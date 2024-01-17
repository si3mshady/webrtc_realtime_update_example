const express = require('express');
const http = require('http');
const cors = require('cors'); // Import the cors package

const port = 3000;

const app = express();
app.use(cors());
app.use('/', express.static(__dirname));
const server = http.createServer(app);

server.listen(port, () => console.log(`Server started on port localhost:${port}`));
