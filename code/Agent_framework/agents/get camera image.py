        cozmo.connect(self.run_cozmo)

    def on_new_camera_image(self, event, *, image: cozmo.world.CameraImage, **kw):
        raw_image = image.raw_image
        self.img2 = cv2.cvtColor(np.array(raw_image), cv2.COLOR_RGB2BGR)
        self.check_image()

    async def set_up_cozmo(self, coz_conn):
        self._robot = await coz_conn.wait_for_robot()
        self._robot.camera.image_stream_enabled = True
        self._robot.add_event_handler(cozmo.world.EvtNewCameraImage, self.on_new_camera_image)
        self._robot.set_head_angle(cozmo.util.Angle(degrees=0))
        return 1

    async def run_cozmo(self, coz_conn):
        await self.set_up_cozmo(coz_conn)
        while True:
            await asyncio.sleep(0)