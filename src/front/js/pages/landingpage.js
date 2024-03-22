import React, { useContext } from "react";
import adncells from "../../img/adncells.jpg"


export const LandingPage = () => {

    return(
        <>
        <div className="landing-page-container">
            <section className="hero">
                <img src={adncells} className="img1"></img>
            </section>
        </div>
        </>
    )

}