document.addEventListener('DOMContentLoaded', function() {
    const data = [
        { week: 1, prevision: 100},
        { week: 2, prevision: 110},
        { week: 3, prevision: 120},
        { week: 4, prevision: 130},
        { week: 5, prevision: 140},
        { week: 6, prevision: 150},
        { week: 7, prevision: 160},
        { week: 8, prevision: 170},
        { week: 9, prevision: 180},
        { week: 10, prevision: 190},
        { week: 11, prevision: 200},
        { week: 12, prevision: 210},
        { week: 13, prevision: 220},
        { week: 14, prevision: 230},
        { week: 15, prevision: 240},
        { week: 16, prevision: 250},
        { week: 17, prevision: 260 },
        { week: 18, prevision: 270 },
        { week: 19, prevision: 280 },
        { week: 20, prevision: 290 },
        { week: 21, prevision: 300 },
        { week: 22, prevision: 310 },
        { week: 23, prevision: 320 },
        { week: 24, prevision: 330 },
        { week: 25, prevision: 340 },
        { week: 26, prevision: 350 },
        { week: 27, prevision: 360 },
        { week: 28, prevision: 370 },
        { week: 29, prevision: 380 },
        { week: 30, prevision: 390 },
        { week: 31, prevision: 400 },
        { week: 32, prevision: 410 },
        { week: 33, prevision: 420 },
        { week: 34, prevision: 430 },
        { week: 35, prevision: 440 },
        { week: 36, prevision: 450 },
        { week: 37, prevision: 460 },
        { week: 38, prevision: 470 },
        { week: 39, prevision: 480 },
        { week: 40, prevision: 490 },
        { week: 41, prevision: 500 },
        { week: 42, prevision: 510 },
        { week: 43, prevision: 520 },
        { week: 44, prevision: 530 },
        { week: 45, prevision: 540 },
        { week: 46, prevision: 550 },
        { week: 47, prevision: 560 },
        { week: 48, prevision: 570 },
        { week: 49, prevision: 580 },
        { week: 50, prevision: 590 },
        { week: 51, prevision: 600 },
        { week: 52, prevision: 610 },
        { week: 53, prevision: 620 },
        { week: 54, prevision: 630 },
        { week: 55, prevision: 640 },
        { week: 56, prevision: 650 },
        { week: 57, prevision: 660 },
        { week: 58, prevision: 670 },
        { week: 59, prevision: 680 },
        { week: 60, prevision: 690 },
        { week: 61, prevision: 700 },
        { week: 62, prevision: 710 },
        { week: 63, prevision: 720 },
        { week: 64, prevision: 730 },
        { week: 65, prevision: 740 },
        { week: 66, prevision: 750 },
        { week: 67, prevision: 760 },
        { week: 68, prevision: 770 },
        { week: 69, prevision: 780 },
        { week: 70, prevision: 790 },
        { week: 71, prevision: 800 },
        { week: 72, prevision: 810 },
        { week: 73, prevision: 820 },
        { week: 74, prevision: 830 },
        { week: 75, prevision: 840 },
        { week: 76, prevision: 850 },
        { week: 77, prevision: 860 },
        { week: 78, prevision: 870 },
        { week: 79, prevision: 880 },
        { week: 80, prevision: 890 },
        { week: 81, prevision: 900 },
        { week: 82, prevision: 910 },
        { week: 83, prevision: 920 },
        { week: 84, prevision: 930 },
        { week: 85, prevision: 940 },
        { week: 86, prevision: 950 },
        { week: 87, prevision: 960 },
        { week: 88, prevision: 970 },
        { week: 89, prevision: 980 },
        { week: 90, prevision: 990 },
        { week: 91, prevision: 1000 },
        { week: 92, prevision: 1010 },
        { week: 93, prevision: 1020 },
        { week: 94, prevision: 1030 },
        { week: 95, prevision: 1040 },
        { week: 96, prevision: 1050 },
        { week: 97, prevision: 1060 },
        { week: 98, prevision: 1070 },
        { week: 99, prevision: 1080 },
        { week: 100, prevision: 1090 },
        { week: 101, prevision: 1100 },
        { week: 102, prevision: 1110 },
        { week: 103, prevision: 1120 },
        { week: 104, prevision: 1130 },
        { week: 105, prevision: 1140 },
        { week: 106, prevision: 1150 },
        { week: 107, prevision: 1160 },
        { week: 108, prevision: 1170 },
        { week: 109, prevision: 1180 },
        { week: 110, prevision: 1190 },
        { week: 111, prevision: 1200 },
        { week: 112, prevision: 1210 },
        { week: 113, prevision: 1220 },
        { week: 114, prevision: 1230 },
        { week: 115, prevision: 1240 },
        { week: 116, prevision: 1250 },
        { week: 117, prevision: 1260 },
        { week: 118, prevision: 1270 },
        { week: 119, prevision: 1280 },
        { week: 120, prevision: 1290 },
        { week: 121, prevision: 1300 },
        { week: 122, prevision: 1310 },
        { week: 123, prevision: 1320 },
        { week: 124, prevision: 1330 },
        { week: 125, prevision: 1340 },
        { week: 126, prevision: 1350 },
        { week: 127, prevision: 1360 },
        { week: 128, prevision: 1370 },
    ];

    const tableBody = document.getElementById('tableHist');
    data.forEach(d => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${d.week}</td>
        <td>${d.prevision}</td>
      `;
      tableBody.appendChild(row);
    });

    const dataTable = new simpleDatatables.DataTable("#myTable", {
      searchable: true,
      fixedHeight: true,
    });
  });


/*
const dataTable = new simpleDatatables.DataTable("#myTable", {
    searchable: true,
    fixedHeight: true,
});


//population de table de historique
  
  const dataHist = [
    // Sample data for 52 weeks
    { week: 1, prevision: 100},
    { week: 2, prevision: 110},
    { week: 3, prevision: 120},
    { week: 4, prevision: 130},
    { week: 5, prevision: 140},
    { week: 6, prevision: 150},
    { week: 7, prevision: 160},
    { week: 8, prevision: 170},
    { week: 9, prevision: 180},
    { week: 10, prevision: 190},
    { week: 11, prevision: 200},
    { week: 12, prevision: 210},
    { week: 13, prevision: 220},
    { week: 14, prevision: 230},
    { week: 15, prevision: 240},
    { week: 16, prevision: 250},
    { week: 17, prevision: 260 },
    { week: 18, prevision: 270 },
    { week: 19, prevision: 280 },
    { week: 20, prevision: 290 },
    { week: 21, prevision: 300 },
    { week: 22, prevision: 310 },
    { week: 23, prevision: 320 },
    { week: 24, prevision: 330 },
    { week: 25, prevision: 340 },
    { week: 26, prevision: 350 },
    { week: 27, prevision: 360 },
    { week: 28, prevision: 370 },
    { week: 29, prevision: 380 },
    { week: 30, prevision: 390 },
    { week: 31, prevision: 400 },
    { week: 32, prevision: 410 },
    { week: 33, prevision: 420 },
    { week: 34, prevision: 430 },
    { week: 35, prevision: 440 },
    { week: 36, prevision: 450 },
    { week: 37, prevision: 460 },
    { week: 38, prevision: 470 },
    { week: 39, prevision: 480 },
    { week: 40, prevision: 490 },
    { week: 41, prevision: 500 },
    { week: 42, prevision: 510 },
    { week: 43, prevision: 520 },
    { week: 44, prevision: 530 },
    { week: 45, prevision: 540 },
    { week: 46, prevision: 550 },
    { week: 47, prevision: 560 },
    { week: 48, prevision: 570 },
    { week: 49, prevision: 580 },
    { week: 50, prevision: 590 },
    { week: 51, prevision: 600 },
    { week: 52, prevision: 610 },
    // Add data for all 52 weeks...
  ];
  const dataL = [
    ["Row 1 Cell 1", "Row 1 Cell 2"],
    ["Row 2 Cell 1", "Row 2 Cell 2"],
    // Add more rows as needed
];
  dataTable.rows.add(dataL);
  /*
 function populateTable(dataHist) {
  const tableBody = document.getElementById('tableHist');
  if (!tableBody) return;

  // Clear existing table data
  while (tableBody.firstChild) {
    tableBody.removeChild(tableBody.firstChild);
  }

  // Populate table with data
  dataHist.forEach(d => {
    const row = document.createElement('tr');
    const weekCell = document.createElement('td');
    const previsionCell = document.createElement('td');

    weekCell.textContent = d.week;
    previsionCell.textContent = d.prevision;

    row.appendChild(weekCell);
    row.appendChild(previsionCell);
    tableBody.appendChild(row);
  });
}

// Initialize table with the first trimester data
document.addEventListener('DOMContentLoaded', function() {
    populateTable(dataHist);
  });
  */