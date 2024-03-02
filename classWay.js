class Player{
    #name;
    #birthDay;
    #monthlySalary;
    #noOfMonths;
    constructor(name, birthDay, monthlySalary, noOfMonths){
        this.#name = name;
        this.#birthDay = birthDay;
        this.#monthlySalary = monthlySalary;
        this.#noOfMonths = noOfMonths;
    }
    calculate_age(){
        const diff_ms = Date.now() - new Date(this.#birthDay).getTime();
        const age_dt = new Date(diff_ms);
        return Math.abs(age_dt.getUTCFullYear() - 1970);
    }
    getSalary(){
        return (this.#monthlySalary * this.#noOfMonths).toLocaleString();
    }
}

const sakib = new Player("Sakib Al Hasan", "1987-10-21", 50000, 12);
const tamim = new Player("Tamim Iqbal", "1985-01-01", 60000, 12);

console.log(sakib.calculate_age());
console.log(sakib.getSalary());
console.log(sakib.name);
console.log(tamim.calculate_age());