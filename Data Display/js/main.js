class Asset {
    constructor(value, assetClass, country, annual_return, risk) {
        this.value = value,
            this.assetClass = assetClass,
            this.country = country,
            this.annual_return = annual_return,
            this.risk = risk
    }
}

assetList = [];

var form = document.querySelector("asset-form");
form.onsubmit = function () {

    value = document.getElementById("value").value
    assetClass = document.getElementById("type").value
    country = document.getElementById("country").value;
    annual_return = .10
    risk = .07

    newAsset = new Todo(assetClass, country, annual_return, risk)
    assetList.push(newTask)
    console.log(assetList)
}