import fetch from 'cross-fetch';

async function postData(url = '', data = '') {
  const response = await fetch(url, {
    method: 'POST',
    headers: {'content-type': 'text/plain', 'Accept-Charset': 'UTF-8'},
    body: data
  });
  return response;
}

var str = "How can you help?";
postData('http://127.0.0.1:5000/api/', str)
  .then(res => res.text())
  .then(data => console.log(data))
  .catch(res => {
    console.log(res);
  });