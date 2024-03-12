import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-expand-lg bg-body-tertiary fixed-top">
		<div className="container">
		  <a className="navbar-brand fs-4" href="#">3D Health</a>
		  <button className="navbar-toggler shadow-none border-0" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
			<span className="navbar-toggler-icon"></span>
		  </button>
		  <div className="sidebar offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
		  {/* Sidebar header */}
			<div className="offcanvas-header text-black border-bottom">
			  <h5 className="offcanvas-title" id="offcanvasNavbarLabel">3D Health</h5>
			  <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
			</div>
			{/* Sidebar body */}
			<div className="offcanvas-body d-flex flex-column p-4">
			  <ul className="navbar-nav justify-content-center align-items-center fs-5 flex-grow-1 pe-3">
				<Link to="/" className="nav-item">
				  <a className="nav-link active">Home</a>
				</Link>
				<Link to="/about" className="nav-item">
				  <a className="nav-link" href="#">About</a>
				</Link>
			  </ul>
			</div>
		  </div>
		</div>
	  </nav>
	);
};
