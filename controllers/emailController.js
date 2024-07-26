import nodemailer from "nodemailer";

export default async function sendEmail(req, res) {
    // Get environment variables
    const smtpServer = process.env.SMTP_SERVER; // SES SMTP endpoint
    const smtpPort = process.env.SMTP_PORT;
    const username = process.env.SMTP_USER; // SES SMTP username
    const password = process.env.SMTP_PASS; // SES SMTP password
    const fromEmail = process.env.EMAIL_SENDER; // Verified email in SES
    const toEmail = "xiaoyang_ho@mymail.sutd.edu.sg"; // Recipient email

    // Create a transporter object using the SMTP server details
    const transporter = nodemailer.createTransport({
        host: smtpServer,
        port: smtpPort,
        secure: false, // Set to true if using port 465
        auth: {
            user: username,
            pass: password
        }
    });

    // Define the email options
    const mailOptions = {
        from: fromEmail,
        to: toEmail,
        subject: 'Hello from Node.js SES SMTP',
        text: 'This is an email sent from Node.js using Amazon SES SMTP in the Asia Pacific (Singapore) region.'
    };

    try {
        // Send the email
        await transporter.sendMail(mailOptions);
        console.log('Email sent successfully to the SES simulator');
        res.status(200).send('Email sent successfully');
    } catch (error) {
        console.error('Failed to send email:', error);
        res.status(500).send(`Failed to send email: ${error.message}`);
    }
}