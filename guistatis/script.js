function hitungMean() {
    // Ambil nilai dari input
    let data1 = parseFloat(document.getElementById('data1').value);
    let data2 = parseFloat(document.getElementById('data2').value);
    let data3 = parseFloat(document.getElementById('data3').value);

    // Hitung mean
    let mean = (data1 + data2 + data3) / 3;

    // Tampilkan hasil
    document.getElementById('mean-output').innerHTML = "Mean: " + mean;
}

function hitungMedian() {
    // Ambil nilai dari input
    let data = [
        parseFloat(document.getElementById('data1').value),
        parseFloat(document.getElementById('data2').value),
        parseFloat(document.getElementById('data3').value)
    ];

    // Urutkan data
    data.sort((a, b) => a - b);

    // Hitung median
    let median;
    if (data.length % 2 === 0) {
        median = (data[data.length / 2 - 1] + data[data.length / 2]) / 2;
    } else {
        median = data[(data.length - 1) / 2];
    }

    // Tampilkan hasil
    document.getElementById('median-output').innerHTML = "Median: " + median;
}

function hitungModus() {
    // Ambil nilai dari input
    let data = [
        parseFloat(document.getElementById('data1').value),
        parseFloat(document.getElementById('data2').value),
        parseFloat(document.getElementById('data3').value)
    ];

    // Hitung frekuensi setiap nilai
    let frekuensi = {};
    for (let i = 0; i < data.length; i++) {
        if (frekuensi[data[i]]) {
            frekuensi[data[i]]++;
        } else {
            frekuensi[data[i]] = 1;
        }
    }

    // Temukan nilai modus
    let modus = null;
    let maxFrekuensi = 0;
    for (let nilai in frekuensi) {
        if (frekuensi[nilai] > maxFrekuensi) {
            modus = nilai;
            maxFrekuensi = frekuensi[nilai];
        }
    }

    // Tampilkan hasil
    if (modus !== null) {
        document.getElementById('modus-output').innerHTML = "Modus: " + modus;
    } else {
        document.getElementById('modus-output').innerHTML = "Modus tidak ditemukan";
    }
}

function hitungStandarDeviasi() {
    // Ambil nilai dari input
    let data = [
        parseFloat(document.getElementById('data1').value),
        parseFloat(document.getElementById('data2').value),
        parseFloat(document.getElementById('data3').value)
    ];

    // Check if there's any valid data
    if (data.some(isNaN)) {
        document.getElementById('stddev-output').innerHTML = "Standar Deviasi: Invalid data found";
        return;
    }

    // Hitung mean
    let mean = hitungMean(data);

    // Hitung kuadrat deviasi dari mean
    let squaredDeviations = [];
    for (let i = 0; i < data.length; i++) {
        let squaredDeviation = Math.pow(data[i] - mean, 2);
        squaredDeviations.push(squaredDeviation);
    }

    // Hitung standar deviasi (handle potential division by zero)
    let variance = squaredDeviations.reduce((sum, value) => sum + value, 0) / (data.length - 1); // Bessel's correction for population standard deviation
    let stddev = Math.sqrt(variance);

    // Tampilkan hasil
    document.getElementById('stddev-output').innerHTML = "Standar Deviasi: " + stddev;
}

