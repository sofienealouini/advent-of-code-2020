for script in(readdir(@__DIR__())) 
    if startswith(script, "day_")
        day_number::String = script[5:6]
        println("\n******* Day $(day_number) *******\n")
        include(script)
        main()
    end
end

println()