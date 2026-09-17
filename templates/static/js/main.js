document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const payload = {
        latitude: parseFloat(document.getElementById('latitude').value),
        longitude: parseFloat(document.getElementById('longitude').value),
        sqft: parseFloat(document.getElementById('sqft').value),
        bedrooms: parseInt(document.getElementById('bedrooms').value)
    };

    const res = await fetch('/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (data.status === 'success') {
        document.getElementById('price').textContent = data.predicted_price;
        document.getElementById('cluster').textContent = data.cluster_id;
        document.getElementById('result').style.display = 'block';
    }
});