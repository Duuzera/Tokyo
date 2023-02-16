function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function renderiza_total_entrada(url){  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('faturamento_total').innerHTML = data.valor
    })

}

function renderiza_total_gastos(url){
    fetch(url, {
        method: 'get',
    }).then (function(result){
        return result.json()
    }).then (function(data){
        document.getElementById('despesa_total').innerHTML = data.valor
    })
}

function renderiza_total_lucro(url){
    fetch(url, {
        method: 'get',
    }).then (function(result){
        return result.json()
    }).then (function(data){
        document.getElementById('lucro_total').innerHTML = data.valor
    })
}


function renderiza_despesas_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('despesas_mensal').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Despesas',
                    data: data.data,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#FFFFFF",
                    borderWidth: 0.2
                }]
            },
        
        });
    })
}

function renderiza_faturamento_mensal(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('faturamento_mensal').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Faturamento",
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 1
                }]
            },
        });


    })


    

}

function renderiza_maiores_entradas(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const ctx = document.getElementById('maiores_entradas').getContext('2d');
        var cores_maiores_entradas = gera_cor(qtd=4)
        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Entradas',
                    data: data.data,
                    backgroundColor: cores_maiores_entradas[0],
                    borderColor: cores_maiores_entradas[1],
                    borderWidth: 1
                }]
            },
            
        });


    })
  
}

function renderiza_maiores_gastos(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        const ctx = document.getElementById('maiores_gastos').getContext('2d');
        var cores_maiores_gastos = gera_cor(qtd=4)
        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Gastos',
                    data: data.data,
                    backgroundColor: cores_maiores_gastos[0],
                    borderColor: cores_maiores_gastos[1],
                    borderWidth: 1
                }]
            },
            
        });


    })
  
}