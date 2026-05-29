import { Request, Response } from "express";
import { T } from "../libs/types/common";

const restaurantController: T = {};
restaurantController.goHome = (req: Request, res: Response) => {
  try {
    res.send("Home Page");
  } catch (err) {
    console.log("Error, goHome:", err);
  }
};

restaurantController.getLogin = (req: Request, res: Response) => {
  try {
    res.send("Log In Page");
  } catch (err) {
    console.log("Error, getLogIn:", err);
  }
};

restaurantController.getSignUp = (req: Request, res: Response) => {
  try {
    res.send("Sign Up Page");
  } catch (err) {
    console.log("Error, getSignUp:", err);
  }
};

export default restaurantController;
