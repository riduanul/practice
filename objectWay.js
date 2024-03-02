const sakib = {
    name : 'Riduanul haque',
    birthDay : '1987-10-21',
    monthlySalary : 40000,
    noOfMonths : 12,

    calculate_age(){
        const diff_ms = Date.now() - new Date(this.birthDay).getTime();
        const age_dt = new Date(diff_ms);
        return Math.abs(age_dt.getUTCFullYear() - 1970);
    },
    
    getSalary(){
        return (this.monthlySalary * this.noOfMonths).toLocaleString();
    }
    
}

console.log(sakib.calculate_age())
console.log(sakib.getSalary())