/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmina <nmina@student.42beirut.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 17:27:18 by nmina             #+#    #+#             */
/*   Updated: 2025/12/24 11:12:19 by nmina            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int ft_printf(const char *format, ...)
{
    va_list args;
    int     count;

    count = 0;
    va_start(args, format);
    while (*format)
    {
        if (*format == '%')
        {
            format++;
            if (*format == 'c')
                count += ft_print_char(va_arg(args, int));
            else if (*format == '%')
                count += ft_print_char('%');
            else if (*format == 's')
                count += ft_print_str(va_arg(args, char*));
            else if (*format == 'p')
                count += ft_print_ptr(va_arg(args, void*));
        }
        else
            count += ft_print_char(*format);
        format++;
    }
    va_end(args);
    return (count);
}

int main(){
    int p = 2;
    ft_printf("%c", 'A');
    ft_printf("%c", '\n');
    ft_printf("%c", 65);
    ft_printf("%c", '\n');
    ft_printf("%s", "hello");
    ft_printf("%c", '\n');
    ft_printf("100%%");
    ft_printf("%c", '\n');
    ft_printf("%p", &p);
    return 0;
}