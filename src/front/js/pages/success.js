import React from "react";
import { Link } from "react-router-dom";

export const Success = () => {

    return(
        <>
        <div className="contact-form-container">
            <div className="contact-confirmation">
                <div className="success">
                    <h1>Thank you for reaching to us</h1>
                    <p>We will respond within the next 24 hours</p>
                    <Link to="/">
                        <button className="btn btn-primary">Back to home</button>
                    </Link>
                </div>
            </div>
        </div>
        </>
    )
}