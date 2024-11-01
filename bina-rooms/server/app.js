const express = require('express');
const cors = require('cors');
const app = express();
const counterRoutes = require('./routes');

app.use(cors());
app.use(express.json());

app.use('/api', counterRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// TODO: I didn't realize all lines yet.