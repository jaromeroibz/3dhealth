import React, {useState, useEffect, useContext} from "react";
import { Context } from "../store/appContext";
import adncells from "../../img/adncells.jpg"

export const ClassSchedule = () => {
    const {store, actions} = useContext(Context)

    useEffect(() => {
        actions.getLessons()
    }, [])

    return(
        <div className="lessons">
            <div className= "available-lessons">
                {store.lessons.map( (lesson) =>
                <div className= "lesson-list">
                    <div className="card" style={{width: "18rem"}}>
                        <div className="card-body">
                            <h5 className="card-title">{lesson.name}</h5>
                            <p className="card-text">{lesson.description}</p>
                            <p className="card-text">{lesson.description}</p>
                            <p className="card-text">${lesson.price}</p>
                            <a href="#" className="btn btn-primary">Book Now</a>
                        </div>
                    </div>
                </div>
                )} 
            </div> 
            <div className="calendar-select">

            </div>          
        </div>

    )
    
}