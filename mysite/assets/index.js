const ctx = document.getElementById('myChart');
const firstChart = document.getElementById('first-Chart');

//on va prendre les données de prévision depuis la base de données
const dataPrevision = [12, 19, 3, 5, 2, 3, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44, 20, 12, 19, 33, 55, 44];
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52'],
    datasets: [{
      label: '# de demande prevu',
      data: dataPrevision,
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
const dataPreviousSemestre = [12, 19, 33, 25, 19, 16, 12, 19, 33, 25, 26, 20, 21];

new Chart(previousData, {
type: 'line',
data: {
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
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
const dataNextSemestre = [12, 19, 33, 30, 28, 30, 25, 19, 33, 36, 44, 40, 38];

new Chart(nextData, {
type: 'line',
data: {
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
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
const dataPerTrimestre = [11, 16, 7, 9];

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
