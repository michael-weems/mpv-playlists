-- NOTE: sane defaults
c = {
	shuffle = false,
	directory = "videos",
}

function print_table(name, t)
	print(name)
	for k, v in pairs(t) do
		print("  " .. k .. ": " .. tostring(v))
	end
end

local i = 1
while i < #arg + 1 do
	if arg[i] == "--shuffle" then
		c.shuffle = true
	elseif arg[i] == "-d" or arg[i] == "--directory" then
		i = i + 1
		c.directory = arg[i]
	end

	i = i + 1
end

print_table("config", c)

function mpv_cmd()
	local cmd = "mpv "

	if c.shuffle then
		cmd = cmd .. " --shuffle"
	end

	cmd = cmd .. " " .. c.directory
	return cmd
end

os.execute(mpv_cmd())
