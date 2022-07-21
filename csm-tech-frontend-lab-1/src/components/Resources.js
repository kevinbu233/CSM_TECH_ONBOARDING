import React from 'react';
import get from "../utils/api";

class Resources extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            activeID: 1
        };
    }

    handleClick(i) {
        this.setState({
            activeID: i
        })
    }

    render() {
        const navbarStyle = {
            color: 'green',
            display: 'flex',
            justifyContent:'center',
            alignItem:'center',
            height: '100px',
        }

        return (
            <div>
                <div className = 'navBar' style = {navbarStyle}>
                    <Navbar  courseID = {this.state.activeID} course = {get("/courses")} onClick = {(i) => this.handleClick(i)}/>
                </div>
                <div>
                    <Table courseID = {this.state.activeID} resource = {get(`/resources/${this.state.activeID}/resources`)}/>
                </div>
            </div>
            
            
        )
    }
}

class Navbar extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        
        let tabs = this.props.course.map((row) => {
            let className = `button`
            if (this.props.courseID === row.id) {
                className += "-active"
            } 
            return <button className = {className} onClick = {() => this.props.onClick(row.id)}>{row.name}</button>
            
        })
        return (
            <div className = "navbar">
                {tabs}
            </div>
        )
    }
}



class Table extends React.Component {
    constructor(props) {
        super(props)
        
    }

    render() {
        const titleName = 
        <thead >
            <tr className="titleRow">
            <th className='title'>Week</th>
            <th className='title'>Date</th>
            <th className='titleTopic'>Topics</th>
            
            <th className='title'>Worksheet and Solutions</th>
        </tr>
        </thead>
        
        const rows = this.props.resource.map((row) =>{
            return <Row info = {row} />
        })
        return (<table className = "content">
            {titleName}
            <tbody>
              {rows}  
            </tbody> 
        </table>)
    }
}

function Row(props) {
    let infos = Object.entries(props.info).map((value) =>{
        if (value[0] === "weekNum")
            return <td className = "info">Week {value[1]}</td>})
    let otherinfos =  Object.entries(props.info).map((value) =>{
        if (value[0] === "date" | value[0] === "worksheet")
            return <td className = "info">{value[1]}</td>
        if (value[0] === "topics")
            return <td className = "topic">{value[1]}</td>})
    return (<tr className = "weeks">{infos}{otherinfos}</tr>)
}

export default Resources;