const ctx = document.getElementById('myChart');
const firstChart = document.getElementById('first-Chart');

// Extract the 'prevision' values from the dictionary
const dataPrevision = window.dicPrevisionTotal.map(item => item.prevision);


// Create the chart
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: window.dicPrevisionTotal.map(item => item.semaine),  // Use the 'semaine' values for the labels
    datasets: [{
      label: '# de demande prévu pendant l année suivante',
      data: dataPrevision,
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      x: {
        title: {
          display: true,
          text: 'Semaine'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Prévision de demande'
        },
        beginAtZero: true
      }
    }
  }
});



//après on va prendre ces données depuis la base de données à partir d'un fichier Json ou API ?
//const dataPreviousSemestre = [41,37,32,20,27,26,20,17,19,26,20,16,16];
var dataPreviousSemestre = window.histData.slice(-13).map(item => item.demande);
console.log(dataPreviousSemestre);


new Chart(previousData, {
type: 'line',
data: {
  labels: window.histData.map(item => item.semaine).slice(-13),
  datasets: [{
    label: 'Qte demande',
    data: dataPreviousSemestre ,
    borderWidth: 1
  }]
},
options: {
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
});

//après on va prendre ces données depuis la base de données à partir d'un fichier Json ou API ?
//const dataNextSemestre = [15, 14, 18, 40, 22, 17, 22, 24, 24, 31, 41, 56, 48];
var dataNextSemestre = window.dicPrevisionTotal.slice(0, 13).map(item => item.prevision);
console.log(dataNextSemestre);

new Chart(nextData, {
type: 'line',
data: {
  labels: window.dicPrevisionTotal.map(item => item.semaine).slice(0, 13),
  datasets: [{
    label: 'Qte demande',
    data: dataNextSemestre ,
    borderWidth: 1
  }]
},
options: {
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
});

//----------------------------------------------
//polar chart

//après on va prendre ces données par calcule et depuis base de données
//const dataPerTrimestre = [372, 945, 772, 327];
function calculateQuarterlySums() {
  const previsionArray = Object.values(window.dicPrevisionTotal);
  const quarterlySums = [];

  for (let i = 0; i < previsionArray.length; i += 13) {
      const quarter = previsionArray.slice(i, i + 13);
      const sum = quarter.reduce((a, b) => a + b.prevision, 0);
      quarterlySums.push(sum);
  }

  return quarterlySums;
}

const dataPerTrimestre = calculateQuarterlySums();
console.log(dataPerTrimestre);

new Chart(polarChart,{
  type: 'polarArea',
  data: {
    labels: [
      'Trimestre 1',
      'Trimestre 2',
      'Trimestre 3',
      'Trimestre 4',
    ],
    datasets: [{
      label: 'Hausse par trimestre',
      data: dataPerTrimestre,
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(75, 192, 192)',
        'rgb(255, 205, 86)',
        'rgb(201, 203, 207)'
      ]
    }]
  },
  options: {}
});
