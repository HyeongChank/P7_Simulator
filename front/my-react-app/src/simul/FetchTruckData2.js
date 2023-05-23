import React, { useState, useEffect } from 'react';
import Display from './Display';

const FetchTruckData2 = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8080/api/truckData')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => setData(data))
            .catch(error => {
                console.error('There has been a problem with your fetch operation: ', error);
            });
    }, []);

    return <Display truckData={data}/>;
    // return(
    //     <div>
    //         hi
    //     </div>
    // )
}

export default FetchTruckData2;
