import express from 'express';
import {sendEmailWithQRCode} from '../controllers/emailController.js';


const router = express.Router();

router.post('/sendQRCode', sendEmailWithQRCode);


export default router;