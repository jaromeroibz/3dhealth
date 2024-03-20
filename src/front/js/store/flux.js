const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			lessons: []
		},
		actions: {
			// Use getActions to call a function within a fuction
			getLessons: async () =>{
				
				const requestOptions = {
					headers: { 'Content-Type': 'application/json'},
					body: JSON.stringify(data)
				}

				let response = await fetch(process.env.BACKEND_URL+'/api/get_lessons', requestOptions)
			
				let data = await response.json()

				if (response.ok){
				  setStore({
					lessons: data
				  })
				  console.log('Lesson exist')
				}
			},
			getAddresses: async () =>{
				
				const requestOptions = {
					headers: { 'Content-Type': 'application/json'},
					body: JSON.stringify(data)
				}

				let response = await fetch(process.env.BACKEND_URL+'/api/get_addresses', requestOptions)
			
				let data = await response.json()

				if (response.ok){
				  setStore({
					addresses: data
				  })
				  console.log('Addresses exist')
				}	
			},
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
