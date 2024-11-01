const counterService = require('../services/tempService');

exports.getCounter = async (req, res) => {
    try {
        const counter = await counterService.getCounter();
        res.status(200).json({ success: true, counter });
    } catch (error) {
        res.status(500).json({ success: false, message: 'Error retrieving counter', error: error.message });
    }
};

exports.incrementCounter = async (req, res) => {
    try {
        const newCounter = await counterService.incrementCounter();
        res.status(200).json({ success: true, counter: newCounter });
    } catch (error) {
        res.status(500).json({ success: false, message: 'Error updating counter', error: error.message });
    }
};
