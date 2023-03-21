
function handle_click(click_event){
    if (click_event.target.id == "btn1"){
        click_event.target.classList.add('blue')

    } else{
        click_event.target.classList.toggle('blue')

    }
    result.innerText = `Button met id ${click_event.target.id} was geklikt! `; //scheve aanhalings teken is zoals de f in python
}


// handle_click({name: 'this is my click_event', id: 1234});

btn1.onclick = handle_click;
btn2.onclick = handle_click;
fake_button.onclick = handle_click;