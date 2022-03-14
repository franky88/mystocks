async function LoadStocks() {
    const response = await fetch("https://phisix-api4.appspot.com/stocks.json");
    const stocks = await response.json();

    return stocks;
}

document.addEventListener("DOMContentLoaded" ,async () => {
    let stocks = [];
    try {
        stocks = await LoadStocks();
    } catch(e) {
        console.log("Error!");
        console.log(e)
    }
    console.log(stocks)
})