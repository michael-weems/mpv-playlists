# NOTE: sane defaults


config = {
	"shuffle" = false,
	"directory" = "videos",
}

argc = len(sys.argv)
for i=1; i<argc; i++
	if sys.argv[i] == "--shuffle"
		config.shuffle = true
	else if sys.argv[i] == "-d" || sys.argv[i] == "--directory"
		i++
		config.directory = sys.argv[i]

# TODO: figure out how to do OS commands
# TODO: convert lua code below to python

function mpv_cmd()
	local cmd = "mpv "

	if c.shuffle then
		cmd = cmd .. " --shuffle"
	end

	cmd = cmd .. " " .. c.directory
	return cmd
end

os.execute(mpv_cmd())
