let stock_symbol = document.getElementById('stock-symbol').innerText;
console.log(stock_symbol);
async function LoadStocks() {
    const response = await fetch("https://phisix-api4.appspot.com/stocks/" + stock_symbol + ".json");
    const stock = await response.json();
    return stock;
}
document.addEventListener("DOMContentLoaded", async () => {
    let stock = [];
    let comm = 0.0025
    let vat = 0.12
    let trans = 0.00005
    let sccp = 0.00010
    let sale_tax = 0.006
    try {
        stock = await LoadStocks();
    } catch(e) {
        console.log("Error!");
        console.log(e)
    }
    if (stock === null) {
        document.querySelector('#current-price').innerText = "Closed";
        document.querySelector('#percent-change').innerText = "Closed";
    } else {
        document.querySelector('#current-price').innerText = stock.stock[0].price.amount;
        document.querySelector('#percent-change').innerText = stock.stock[0].percent_change;
        let avg_price = document.querySelector('#avg-price').innerText;
        let total_share = document.querySelector('#total-share').innerText;
        let total_investment = document.querySelector('#total-invs').innerText;
        let comm_fee = stock.stock[0].price.amount * parseFloat(total_share) * comm;
        console.log("commission fee", comm_fee);
        if (comm_fee < 20) {
            comm_fee = 20.0;
        } else {
            comm_fee;
        }
        console.log("commission fee new", comm_fee)
        let trans_fee = parseFloat(total_share) * stock.stock[0].price.amount * trans;
        let sccp_fee = parseFloat(total_share) * stock.stock[0].price.amount * sccp;
        let sale_tax_fee = parseFloat(total_share) * stock.stock[0].price.amount * sale_tax;
        let total_fees = comm_fee + (comm_fee * vat) + trans_fee + sccp_fee + sale_tax_fee;
        console.log("total fee", total_fees);
        let market_value = (parseFloat(total_share) * stock.stock[0].price.amount) - total_fees;
        document.querySelector('#market-value').innerText = market_value;
        let gain_loss = market_value - parseFloat(total_investment);
        document.querySelector('#gain-loss').innerText = gain_loss;
        if (gain_loss < 0) {
            document.getElementById('gain-loss').style.color = "red";
        } else {
            document.getElementById('gain-loss').style.color = "green";
        }
    }
    console.log(stock.stock[0])
})