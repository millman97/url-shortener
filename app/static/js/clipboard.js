btn = document.getElementById('copy-to-clipboard')
url = document.getElementById('short-url-text').textContent

btn.addEventListener('click',() => copyToClipboard(url))

function copyToClipboard(url){
    navigator.clipboard.writeText(url);
}
