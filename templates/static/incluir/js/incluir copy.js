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

function add_cat_ent(){
    categoria = document.getElementById('cat')

    fetch('incluir_categoria_entrada/' + id, {

        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            categoria : categoria
        })

    }).then(function(result){
        return result.Json()
    }).then(function(data){
        if(data['status'] == '200'){
            categoria = data ['categoria']
        }else{
            console.log('Ocorreu algum erro')
        }
        
    })
}