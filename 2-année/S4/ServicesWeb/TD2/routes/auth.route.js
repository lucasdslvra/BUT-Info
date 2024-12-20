const {verifySignUp} = require("../middleware");
const controller = require("../controllers/auth.controllers.js");
module.exports = function (app) {
    app.use(function (req, res, next) {
        res.header(
            "Access-Control-Allow-Headers",
            "x-access-token, Origin, Content-Type, Accept"
        );
        next();
    });

    app.post(
        "/auth/signup",
        [
            verifySignUp.checkDuplicateUsername,
        ],
        controller.signup
    );
    app.post("/auth/signin", controller.signin);
};