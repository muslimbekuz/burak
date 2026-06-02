import { Request, Response } from "express";
import { T } from "../libs/types/common";
import MemberService from "../models/Member.service";

const restaurantController: T = {};
restaurantController.goHome = (req: Request, res: Response) => {
  try {
    console.log("goHome");
    res.send("Home Page");
    // send | json | redirect | end | render
  } catch (err) {
    console.log("Error, goHome:", err);
  }
};

restaurantController.getLogin = (req: Request, res: Response) => {
  try {
    console.log("getLogin");
    res.send("Log In Page");
  } catch (err) {
    console.log("Error, getLogIn:", err);
  }
};

restaurantController.getSignUp = (req: Request, res: Response) => {
  try {
    console.log("getSignup");
    res.send("Sign Up Page");
  } catch (err) {
    console.log("Error, getSignUp:", err);
  }
};

restaurantController.processLogin = (req: Request, res: Response) => {
  try {
    console.log("processLogin");
    res.send("Done processLogin");
  } catch (err) {
    console.log("Error, processLogin:", err);
  }
};

restaurantController.processSignUp = (req: Request, res: Response) => {
  try {
    console.log("processSignUp");
    res.send("Done processSignUp");
  } catch (err) {
    console.log("Error, processSignUp:", err);
  }
};

export default restaurantController;
