async function test() {
    const response = await fetch('http://localhost:8080/api/truckData');

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
    return data;
}

// 사용 예
test().catch(error => {
    console.error('There has been a problem with your fetch operation: ', error);
});
