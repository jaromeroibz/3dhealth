import React, { useRef } from 'react';
import emailjs from '@emailjs/browser';
import { useNavigate } from 'react-router-dom';

export const ContactForm = () => {
  const form = useRef();
  const navigate = useNavigate()


  const sendEmail = (e) => {
    e.preventDefault();

    emailjs
      .sendForm('service_ixesjxk', 'template_7t8n7sp', form.current, {
        publicKey: '7ndeBbuWPdG-_I8_j',
      })
      .then(
        () => {
          console.log('SUCCESS!');
        },
        (error) => {
          console.log('FAILED...', error.text);
        },
      );
    
    navigate('/success')
  };

  return (
    <>
    <h1>Contact Us</h1>
    <p>Lorem ipsum</p>
    <div className='contact-form-container'>
      <form className='contactform' ref={form} onSubmit={sendEmail}>
        {/* <label>Name</label>
        <input type="text" name="user_name" />
        <label>Email</label>
        <input type="email" name="user_email" />
        <label>Message</label>
        <textarea name="message" />
        <input type="submit" value="Send" placeholder='Message' /> */}
        <div className="mb-3">
          <label htmlFor="exampleFormControlInput1" className="form-label">Name</label>
          <input type="text" name="user_name" className="form-control" placeholder="Write your name" required></input>
        </div>
        <div className="mb-3">
          <label htmlFor="exampleFormControlInput2" className="form-label">Email address</label>
          <input type="email" name="user_email" className="form-control" placeholder="name@example.com" required></input>
        </div>
        <div className="mb-3">
          <label htmlFor="exampleFormControlTextarea1" className="form-label">Example textarea</label>
          <textarea className="form-control" name="message" id="textarea" rows="3" placeholder="Write your concerns" required></textarea>
        </div>
        <div className="mb-3">
        <button className="btn btn-primary" type="submit" value="Send">Submit form</button>
        </div>
      </form>
    </div>
    </>
  );
};