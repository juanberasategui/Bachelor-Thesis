Dataset = read.csv("price_data.csv",sep = ";")
Dataset
handel <- c("size","value","prof", "inv")

i=1 

var <- quo(handel[i])
Dataset_Loop <- Dataset %>% select("date", gvkey, market_value, lag1.market_value, ret, isin, !!var) 
Dataset_Loop <- Dataset_Loop %>% rename(sortVar = !!var) %>% mutate(missing= ifelse(is.na(sortVar) ==T, 1, 0))
breakpoints <- Dataset_Loop %>%  group_by(date) %>% 
  summarize(var.P70 = quantile(eval(sortVar), probs=.7, na.rm=TRUE),
            var.P30 = quantile(eval(sortVar), probs=.3, na.rm=TRUE),
            number_of_stocks = n(),
            missingSortVar = sum(missing))
final_thing_breakpoints <- Dataset_Loop %>% left_join(breakpoints, by= 'date')
final_thing_breakpoints <- final_thing_breakpoints %>%
  mutate(Var = ifelse(eval(sortVar) < var.P30,"Low", ifelse(eval(sortVar) > var.P70, "High", "Neutral")))

final_thing_breakpoints
write.csv(final_thing_breakpoints, "FF_Size_INT.csv")
