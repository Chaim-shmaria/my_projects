const express = require('express');
const router = express.Router();
const tempController = require('../controllers/tempController');

router.get('/', tempController.getCounter);
router.post('/increment', tempController.incrementCounter);

module.exports = router;

// TODO: change the name 'counter'.