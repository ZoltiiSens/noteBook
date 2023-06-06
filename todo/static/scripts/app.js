'use strict'

/**
 * Closes currently active popup
 */
function closePopup(){
	document
		.getElementById('active_background')
		.removeAttribute('id');
	document
		.getElementById('active_popup')
		.removeAttribute('id');
}

/**
 * Making week creation popup active
 */
function createWeek(){
	document
		.getElementsByClassName('creation_popup')[0]
		.setAttribute('id', 'active_popup');
	document
		.getElementsByClassName('popup_background')[0]
		.setAttribute('id', 'active_background');
}

/**
 * Making week editing popup active
 * @param {number} week_pk Primary key for week we edit
 */
function editWeek(week_pk){
	document
		.getElementsByClassName(`editing_popup--${week_pk}`)[0]
		.setAttribute('id', 'active_popup');
	document
		.getElementsByClassName('popup_background')[0]
		.setAttribute('id', 'active_background');
}

/**
 * Making todo editing popup active
 * @param {number} todo_pk Primary key for todo we edit
 */
function editTodo(todo_pk){
	document
		.getElementsByClassName(`editing_popup--${todo_pk}`)[0]
		.setAttribute('id', 'active_popup');
	document
		.getElementsByClassName('popup_background')[0]
		.setAttribute('id', 'active_background');
}

/**
 * Changes day in todo to the next state
 * @param {number} todo_pk Primary key for todo we edit
 * @param {number} day_pk Number of the day we change
 */
function editDay(todo_pk, day_pk){
	let day_input = document.getElementById(`input_day--${ todo_pk }--${day_pk}`);
	let day_img = document.getElementById(`img_day--${ todo_pk }--${day_pk}`);
	let current_val = 0;
	// cycle for current_val 0>1>2>3>4>5>0>1>...
	if (day_input.value !== "5"){
		current_val = +day_input.value + 1;
	}
	day_input.value = current_val;
	day_img.src = `/static/images/${current_val}.svg`
}