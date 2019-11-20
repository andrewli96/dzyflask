const express = require('express')
const request = require('request')
const bodyParser = require('body-parser')
const axios = require('axios');

const app = express()

const username = 'dzyadmin'
const password = 'admin1234'

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));



app.post('/api/upload', (req, res) => {
    console.log(req.body.path, req.body.name)
    axios.post('http://localhost:3001/auth', {
        username: username,
        password: password,
      })
      .then(function (response) {
        console.log(response.data.access_token)
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access_token
        axios.post('http://localhost:3001/api/v1/unrar', 
            {
                path: req.body.path,
                name: req.body.name,
            })
            .then(function (resp) {
                console.log('ok');
                res.send(resp.data)
            })
            .catch(function (error) {
                console.log('error_');
                res.send(error)
            });
        })
        .catch(function (error) {
            console.log(error);
            res.send('error')
        });
      
})

app.listen(3000, console.log(3000))