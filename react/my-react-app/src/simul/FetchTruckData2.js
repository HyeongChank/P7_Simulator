import React, { useState, useEffect } from 'react';

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

    return (
        <div>
            {data.map((item, index) =>{
                return(
                <div key={index}>
                <p>{item.number}</p>
                <p>{item.code}</p>
                <p>{item.entryTime}</p>
                <p>{item.visible}</p>
                </div>
                )
            })}
 
        </div>
    );
}

export default FetchTruckData2;
