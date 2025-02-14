"use strict";

const errorMESGeL = document.querySelector('.error_message');
const budgetInputEl = document.querySelector('.budget_input');
const expenseDelEl = document.querySelector('.expenses_input');
const expenseAmountEl = document.querySelector('.expenses_amount');

const tblRecordEl = document.querySelector('.tbl_data');
const cardsContainer = document.querySelector('.cards');

const budgetCardEl = document.querySelector('budget_card');
const expenseCardEl = document.querySelector('.expenses_card');
const balance = document.querySelector('.balance_card');

let itemList = [];
let itemId = 0;

function btnEvents(){
    const btnBudgetCal = document.querySelector('#btn_budget');
    const btnExpensesCal =  document.querySelector('#btn_expenses');


    btnBudgetCal.addEventListener('click',(e) => {
            
    e.preventDefault();
    budgetFun();
   

    });

    btnExpensesCal.addEventListener('click', (e) => {
        console.log("expenses");

    });

}



document.addEventListener("DOMContentLoaded", btnEvents);


function budgetFun() {
    
    const budgetValue = budgetInputEl.Value;
    
    if (budgetValue == "" || budgetValue < 0){
        errorMESGeL.innerHTML = "<p>please enter budget or be more than 0</p>";
        
    }else
    {
        budgetCardEl.textContent = budgetValue;
        budgetInputEl.Value = "";
        showBalance();
    }
}

function showBalance(){
    const expenses = totalExpenses();
}

function totalExpenses(){
    let total = 50;
    return total;
}
