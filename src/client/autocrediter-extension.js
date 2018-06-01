const creditAuthor = () => {
    const htmlCredit = $('.copy ~ input').last().val()
    fetch('http://localhost:8080?=' + htmlCredit)   
}

$('button').on('click', e => {
    console.log('but', e.target)
    if (e.target.parentElement.id === 'download-free'
    || e.target.id === 'download-free') {
        creditAuthor()
    }
})

$(document).on('click', e => {
    console.log('doc', e.target)
    if (e.target.parentElement.id === 'download-free'
    || e.target.id === 'download-free') {
        creditAuthor()
    }
})
