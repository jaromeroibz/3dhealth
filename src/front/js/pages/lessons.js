import React, {useState, useEffect, useContext} from "react";
import { Context } from "../store/appContext";

export const Lessons = () => {
    const {store, actions} = useContext(Context)

    useEffect(() => {
        actions.getLessons()
    }, [])

    return(
        <div className="lessons">
            {store.lessons.map( (lesson) =>
            <div className= "lesson-container">
                <div className="img-container">
                    <img className="lesson-img" src="https://images.pexels.com/photos/132477/pexels-photo-132477.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"></img>
                </div>
                <div className="description px-5">
                    <h3>{lesson.name}</h3>
                    <p className="card-text">{lesson.description}</p>
                    <p className="card-text">${lesson.price}</p>
                    <div className="px-3 d-flex">
                        <a href="#" className="btn btn-primary">Book Now</a>
                    </div>    
                    <div className="px-3">
                        <a href="#" className="btn btn-primary">More Details</a>
                    </div>
                </div>
            </div>
            )} 
        <div className="calendar-select">

        </div>          
        </div>

    )
    
}