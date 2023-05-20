const fs = require('fs');
const csv = require('csv-parser');

const trucksData = [];

fs.createReadStream('C:/git clone/P7_simulation/P7_Simulator/sorted_truck_simulation_results.csv')
  .pipe(csv())
  .on('data', (row) => {
    console.log(row)
    // row object contains the parsed data of a line.
    // You may need to modify this code depending on the structure of your CSV file.
    trucksData.push({
      number: row.Truck_Num,
      code: row.Code,
      entryTime: row.In_time *1000,
      visible: 'true'
    });
  })
  .on('end', () => {
    console.log(trucksData);
  });
