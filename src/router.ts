import express from "express";
const router = express.Router();
import memberController from "./controllers/member.controller";

/* Member */
router.post("/member/login", memberController.Login);
router.post("/member/signup", memberController.SignUp);
router.get("/member/detail", memberController.verifyAuth);

export default router;
