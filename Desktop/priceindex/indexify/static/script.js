// Price Chart (replace with your data source)
const ctx = document.getElementById('priceChart').getContext('2d');
const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];

// Replace with your data fetching logic (example using dummy data)
const domesticPrices = [10, 12, 15, 13, 11, 14];
const internationalPrices = [11, 13, 14, 12, 10, 13];

const data = {
  labels: labels,
  datasets: [{
    label: 'Domestic Price',
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    data: domesticPrices,
  }, {
    label: 'International Price',
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    data: internationalPrices,
  }]
};

const config = {
  type: 'line',
  data: data,
  options: {
    responsive: true,
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
};

new Chart(ctx, config);

// Market News (replace with your API call or news source)
const newsList = document.getElementById('newsList');

// Example using dummy news data
const newsData = [
  { title: "Global Wheat Prices Rise on Supply Concerns", url: "https://..." },
  { title: "New Techniques Improve Crop Yields in Africa", url: "https://..." },
];

newsData.forEach(newsItem => {
  const newsListItem = document.createElement('li');
  const newsLink = document.createElement('a');
  newsLink.href = newsItem.url;
  newsLink.textContent = newsItem.title;
  newsListItem.appendChild(newsLink);
  newsList.appendChild(newsListItem);
});

// Agriculture Tips (replace with your API call or data source)
const tipList = document.getElementById('tipList');

// Example using dummy tips data
const tipData = [
  "Practice crop rotation to improve soil health.",
  "Use organic fertilizers for sustainable farming.",
  "Monitor weather conditions to optimize irrigation practices.",
];

tipData.forEach(tip => {
  const tipListItem = document.createElement('li');
  tipListItem.textContent = tip;
  tipList.appendChild(tipListItem);
});

