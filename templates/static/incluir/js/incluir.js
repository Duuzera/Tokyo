
function exibir_form(tipo){

    add_entradas = document.getElementById('adicionar-entradas')
    add_gastos = document.getElementById('adicionar-gastos')


    if (tipo == "1"){
        add_gastos.style.display = "none"
        add_entradas.style.display = "block"
        

    }else if (tipo == "2"){
        add_gastos.style.display = "block"
        add_entradas.style.display = "none"
        

    }
}