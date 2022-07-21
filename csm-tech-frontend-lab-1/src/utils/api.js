import courses from "../data/courses";
import resources from "../data/resources";

const get = (endpoint) => {
    if (endpoint === '/courses') {
        return courses;
    } else if (endpoint.includes('/resources')) {
        const re = /\d/;
        const course_id = re.exec(endpoint)
        return resources[course_id];
    } else {
        return 'invalid GET request url';
    }
}

export default get;