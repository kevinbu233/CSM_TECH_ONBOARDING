Response format:
[
	{
		id: int,
		user: {
			id: int,
			username: string,
			email: string,
			// ... other fields
		},
		section: {
			id: int,
			mentor: {
				// ... other fields
			}
		},
		// ... other fields
	},
	...
]