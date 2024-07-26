import express from 'express';
import sendEmail from '../controllers/emailController.js';


const router = express.Router();

// router.get('/:email/:msg', sendEmail);
router.get('/email', sendEmail);


export default router;