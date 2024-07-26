import express from 'express';
import cors from 'cors';
import emailRoutes from './routes/emailRoutes.js';
import whatsappRoutes from './routes/whatsappRoutes.js';
const app = express();
const PORT = 3000;
import dotenv from 'dotenv';

// Load environment variables from .env file
dotenv.config();

app.use(cors({
    origin: 'http://localhost:3000'
  }));

app.get('/', (req, res) => {
    res.send('Express App containing api calls for Twilio and SMTP');
  });

// Middleware
app.use(express.json());

// Routes
app.use('/email', emailRoutes);

// Routes
app.use('/whatsapp', whatsappRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});