import express from "express";
const router = express.Router();
import memberController from "./controllers/member.controller";

router.post("/login", memberController.Login);
router.post("/signup", memberController.SignUp);

export default router;
