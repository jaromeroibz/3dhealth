import React, { useContext } from "react";
import adncells from "../../img/adncells.jpg"


export const LandingPage = () => {

    return(
        <>
        <div className="landing-page-container">
            <h1>3D Health</h1>
            <section className="hero">
                <img src={adncells} className="img1"></img>
            </section>
        </div>
        </>
    )

}